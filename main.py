from instapy import InstaPy
password = "put your password here"

session = InstaPy(username="putyourusernamehere",
                  password=password)
session.login()
session.like_by_tags(["coding", "python"], amount=5)
