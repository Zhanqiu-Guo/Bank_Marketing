from explainerdashboard import ClassifierExplainer, ExplainerDashboard
explainer = ClassifierExplainer.from_file("explainer.joblib")
# you can override params during load from_config:
db = ExplainerDashboard.from_config(explainer, "dashboard.yaml", title="Awesomer Title")
app = db.flask_server()