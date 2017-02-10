from git import Repo;
import traceback, sys

repo = Repo("/Users/alekh.raj/Documents/tagtesting");
git = repo.git
git.tag("-s", "-a", "tag_8", "-m", "this is 8th tag", "0407455742f84f78b2652cb4563545766ec9aca6");
git.push("origin", "tag_8")

#def func(e):
#	print traceback.format_exc();

#try:
#	repo = Repo("/Users/alekh.raj/Documents/tagtesting");
#except Exception as e:
#	func(e);


#print repo;

#tags = repo.tags

#print tags;
#print repo;

#git = repo.git;

#try:
#	print "response = ", resp;
#except Exception as e:
#	message = traceback.format_exc();
#	print "***********************************";
#
#	print "message = ", message
#	print type(e)
#	pass;

#print "***********************************";


#git.push("origin", "--tags");
#git.push("origin", "python_tag_3");

#tags = repo.tags;

#print "response = ", resp;