import requests;
import datetime;

class GitTag:

	def __init__(self, gitUser, gitRepoName, authNToken = ""):
		self.gitUser = gitUser;
		self.gitRepoName = gitRepoName;
		self.authNToken = authNToken;

		#self.postTagUrl = "https://api.github.com/repos/{}/{}/git/tags".format(self.gitUser, self.gitRepoName);
		#self.postRefUrl = "https://api.github.com/repos/{}/{}/git/refs".format(self.gitUser, self.gitRepoName);
		#self.getTagUrl = "https://api.github.com/repos/{}/{}/git/tags".format(self.gitUser, self.gitRepoName);


	def getTag(self, tagSHA):
		getTagUrl = "https://api.github.com/repos/{}/{}/git/tags/{}".format(self.gitUser, self.gitRepoName, tagId);
		r = requests.get(getTagUrl, auth = (self.gitUser, self.authNToken));
		jsonObj = r.json();
		print r, r.text, jsonObj.get("tagger"), r.status_code;

	def createRef(self, tagSHA, tag):
		postRefUrl = "https://api.github.com/repos/{}/{}/git/refs".format(self.gitUser, self.gitRepoName);

		payload = {};
		payload["ref"] = "refs/tags/{}".format(tag);
		payload["sha"] = tagSHA;

		response = requests.post(postRefUrl, json = payload, auth = (self.gitUser, self.authNToken));
		print response.json();


	def createTag(self, commitSHA, tag, message, taggerName, taggerEMail):
		payload = {};

		tagger = {};
		tagger["name"] = taggerName;
		tagger["email"] = taggerEMail;
		tagger["date"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ");

		payload["tag"] = tag;
		payload["message"] = message;
		payload["object"] = commitSHA;
		payload["type"] = "commit";
		payload["tagger"] = tagger;

		postTagUrl = "https://api.github.com/repos/{}/{}/git/tags".format(self.gitUser, self.gitRepoName)

		

		response = requests.post(postTagUrl, json = payload, auth = (self.gitUser, self.authNToken));
		tagSHA = response.json().get("sha");
		print tagSHA, response.json(); 

		self.createRef(tagSHA, tag);


g = GitTag("alekh2", "tagtest", "auth_token");
g.createTag("fba20ae7cfa545198d2f0f98c9d7086aa2e9f268", "tag-3", "testing tag signing 1", "Alekh Raj", "alekh.raj@flipkart.com");
