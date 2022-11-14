from deta import Deta

#TODO: Move this to it's own module/file that handles database access
#       and data formatting.
dta = Deta()
dta_db = dta.Base("MothRaces")

def app(event):
    return "Hello, world!"

