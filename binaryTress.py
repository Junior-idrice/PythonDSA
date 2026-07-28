'''
Consider the problem below
As a senior engineer at google, you are tasked with developing a fast in-memory
 data structure to manage profile information(username, name and email) for100 million users.
 it should allow the following operation to be performed efficiently

 1- Insert the profile information for a new user
 2- Find the profile information of a user, given their username
 3- Update the profile information of a user, give their username
 4- List all the users of the platform, sorted by username

 you can assume that usernames are unique 

'''
# Solution

class User:
      def __init__(self, username, name, email):
            self.name = name 
            self.username = username
            self.email = email

      def __repr__(self):
            return "User(username='{}', name='{}') ".format(self.username, self.name)
      def __str__(self):
            return self.__repr__()
class UserDatabase:
    def insert(self, user):
        pass
    def find(self, username):
            pass
    def update(self, user):
            pass
    def lsit_all(self):
            pass

#sample of inputs 


class UserDatabase:
    def __init__(self):
            self.users = []
    def insert(self, user):
          i = 0
          while i< len(self.users):
                if self.users[i].username > user.username:
                      break
                i +=1
          self.users.insert(i,user)

    def find(self,username):
        for user in self.users:
              if user.username == username:
                    return user

    def update(self,user):
          target = self.find(user.username)
          target.name, target.email = user.name, user.email

    def list_all(self):
          return self.users


user1 = User('feujio','dong','dongmo18')
user2 = User('youyou','ituka','youyou18')
user3 = User('farel','urbain','farel18')
users = [user1,user2,user3]

db = UserDatabase()
for user in users:
    db.insert(user)
#print(db.list_all())

print(db.find('feujio'))