from git import Repo;
import traceback;

class GitTagWithoutApi:
	def __init__(localRepoPath):
		try:
			self.repo = Repo(localRepoPath);
			return createObjectCreationSuccessResponse();
		except Exception as e:
			return createExceptionResponse(e);

	def createObjectCreationSuccessResponse():
		response = {};
		response["msg"] = "Object created Successfully";
		response["status"] = 0
		return response

	def createExceptionResponse(e):
		response = {};
		response["msg"] = traceback.format();
		response["status"] = 1
		return response

	def createMissingFieldResponse(field):
		response = {};
		response["msg"] = "{} can't be empty".format(field);
		response["status"] = 1
		return response

	def pushTag(remote = "", tagName):
		try:
			git = self.repo.git;
			git.push(remote, tagName);
		except Exception as e:
			return createExceptionResponse(e);

	def createTag(self, commitSHA, tagMsg, tagName, remote=""):
		if not commitSHA:
			return createMissingFieldResponse("commitSHA");

		if not tagMsg:
			return createMissingFieldResponse("tagMsg");

		if not tagName:
			return createMissingFieldResponse("tagName");
		
		try:
			git = self.repo.git;
			git.tags("-s", "-a", tagName, "-m", tagMsg, commitSHA);
			pushTag(remote, tagName);
		except Exception as e:
			return createExceptionResponse(e);	

	def deleteTag(self, tagName, remote=""):
		try:
			git = self.repo.git;
			git.tag("-d", tagName);
			pushTag(remote, tagName);
		except Exception as e:
			return createExceptionResponse(e);



