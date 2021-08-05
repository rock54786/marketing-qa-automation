import requests
import json
from config import ENV
import os


class TrackingNumUtil:
    @classmethod
    def __get_sample_tracking_nums(cls, slug=None, status=None):
        url = "https://aftership-admin.automizelyapi.org/v1/sample-tracking-numbers"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
                          "Chrome/91.0.4472.164 Safari/537.36 ", "authorization": ENV.AUTHORIZATION}
        params = {"page": 1, "limit": 50}
        if not slug:
            params["slugs"] = slug
        if not status:
            params["statuses"] = status

        resp = requests.get(url, params=params, headers=headers)
        assert resp.status_code == 200, resp.text
        tracking_nums = resp.json()["data"]["sample_tracking_numbers"]
        return tracking_nums

    @staticmethod
    def get_tracking_nums(slug=None, status=None):
        """
        Get tracking numbers from cache. If do not exist, will get from remote
        """
        nums = []
        cache_filename = os.getcwd()
        if "tests" in cache_filename:
            cache_filename = cache_filename + os.path.sep + ("tracking_num_cache.json")
        else:
            cache_filename = cache_filename + os.path.sep + "tests" + os.path.sep + ("tracking_num_cache.json")
        if os.path.exists(cache_filename):
            with open(cache_filename) as f:
                content = f.read()
                cache_nums = json.loads(content)
                for x in cache_nums:
                    if not x["used"]:
                        if not slug and not status:
                            nums.append(x)
                        elif not slug and status and (x["status"] == status):
                            nums.append(x)
                        elif not status and (x["slug"] == slug):
                            nums.append(x)
                        elif (x["status"] == status) and (x["slug"] == slug):
                            nums.append(x)
                if len(nums) == 0:  # if no data, get and store them
                    for x in TrackingNumUtil.__get_sample_tracking_nums(slug, status):
                        nums.append(
                            {'tracking_number': x["tracking_number"], 'slug': x["slug"], 'status': x["latest_status"],
                             'used': False})
                        cache_nums.append(
                            {'tracking_number': x["tracking_number"], 'slug': x["slug"], 'status': x["latest_status"],
                             'used': False})
        else:
            cache_nums = []
            for x in TrackingNumUtil.__get_sample_tracking_nums(slug, status):
                nums.append(
                    {'tracking_number': x["tracking_number"], 'slug': x["slug"], 'status': x["latest_status"],
                     'used': False})
                cache_nums.append(
                    {'tracking_number': x["tracking_number"], 'slug': x["slug"], 'status': x["latest_status"],
                     'used': False})
        with open(cache_filename, 'w') as f:
            json.dump(cache_nums, f, indent=4)
        return nums

    @staticmethod
    def disable_in_cache(tracking_num):
        """
        Set the tracking num as used
        """
        cache_nums = []
        cache_filename = os.getcwd()
        if "tests" in cache_filename:
            cache_filename = os.path.join(cache_filename, "tracking_num_cache.json")
        else:
            cache_filename = os.path.join(cache_filename, "tests", "tracking_num_cache.json")
        with open(cache_filename) as f:
            content = f.read()
            cache_nums = json.loads(content)
            for x in cache_nums:
                if tracking_num == x["tracking_number"]:
                    x["used"] = True
        with open(cache_filename, 'w') as f:
            json.dump(cache_nums, f, indent=4)
