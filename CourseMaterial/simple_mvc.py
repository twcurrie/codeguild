# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE
class Model(object):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.objects = []

    def create(self, item):
       self.objects.append(item)


                   # VIEW: A TEMPLATE FOR A PAGE OR PAGE 
class View(object):
    def __init__(self, template, model):
        self.template = template
        self.model = model

    def render(self):
        output = ""
        for item in self.model.objects:
           item_template = self.template
           
            for field in self.model.fields:
                if item.has_key(field):
                    item_template = item_template.replace("{{" + field + "}}", item[field])
            output += item_template
        return output

# CONTROLLER: Routes messages

class Controller(object):
    def __init__(self):
        self.routes = {}

    def route(self, path):
        return self.routes[path].render()
    
# CONTAINS THE SINGLE CONTROLLER AND ALL MODEL AND VIEW INSTANCES
class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.controller = Controller()

# CREATE AN APPLICATION INSTANCE
app = Application()

# define models (
app.models["user"] = Model("user", ["name", "score"])
app.models["game"] = Model("game", ["game_name", "description"])

# load model objects form database tables
app.models["user"].objects = [{"name": "Bob", "score": "9"},
                                {"name": "Carol", "score": "11"},
                                {"name": "Ted", "score": "15"},
                                {"name": "Alice", "score": "13"}]

scoresTemplate = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>.<br>\n"
model = app.models["user"]
scoresView = View(scoresTemplate, model)
scoresURL = "/scores/"
app.controller.routes = {
        scoresURL: scoresView
        }

request_path = "/scores/"
print(app.controller.route(request_path))
