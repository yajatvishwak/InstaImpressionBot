from instapy import InstaPy
password = "yajat12345#"

session = InstaPy(username="thisisyajatvishwakk",
                  password=password)
session.login()
session.like_by_tags(["coding", "python"], amount=5)
