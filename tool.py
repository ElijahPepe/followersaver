import json
import sys
import snscrape.modules.twitter as sntwitter

def main():
	source_file = sys.argv[1]

	with open(source_file, "r") as file:
		f = file.read()
		follows = json.loads(f)

	for follow in follows:
		try:
			user = sntwitter.TwitterProfileScraper(follow["following"]["accountID"], True)
			username = user._get_entity().username
			follow["following"] |= { "username": username }
			display_name = user._get_entity().displayname
			follow["following"] |= { "displayName": display_name }
		except:
			pass

	with open(source_file, "w") as file:
		json.dump(follows, file, indent=4)

if __name__ == "__main__":
	main()