#importing feedparser - Parse Atom and RSS feeds in Python
import feedparser
import webbrowser

#used to create front bannner.
from pyfiglet import Figlet
print("\n* Copyright of Anurag mhatre, 2021-----------------------------*".upper())
print("\n* https://dev-breathtechsolution.pantheonsite.io")
print("\n* https://github.com/anuragmhatre")

#creating a custom banner.
custom = Figlet(font='graffiti')
print(custom.renderText('Cyberwar - Up2date'.upper()))
print("\n*--CyberSecurity News and articles Website List--")
print("[0]: ThreatPost")
print("[1]: NakedSecurity")
print("[2]: TheHackerNews")
def main():
    print("--Security News Website List--")
    print("[0]: TheHackerNews")
    print("[1]: ThreatPost")
    print("[2]: NakedSecurity")

#creating website list just to provide feeds to user
website_list = ("https://feeds.feedburner.com/TheHackersNews", "https://threatpost.com/feed", "https://nakedsecurity.sophos.com/feed")

website_input = int(input("Enter website by number for news (0-3): "))

#Using feedparser to fetch data from Website_List when user enter data in WebsiteInput
NewsFeed = feedparser.parse(website_list[website_input])
article_list = []
article_link = []
for i in range(5):
    article = NewsFeed.entries[i]
    titles = article.title
    link = article.link
    article_link.append(link)
    article_list.append(titles)

    article_num = 1
    for article in article_list:
        print('[{}] {}'.format(str(article_num), article))
        article_num += 1

    article_link_click = False
    while not article_link_click:
        user_click = int(input("Choose the link you want to open (0-3): "))
        webbrowser.open(article_link[user_click-1])
        article_link_click = True
        break

main()


