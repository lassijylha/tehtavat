from urllib import request
import tomli
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = tomli.loads(content)

        project = data["project"]

        name = project["name"]
        description = project["description"]
        dependencies = project["dependencies"]
        dev_dependencies = data["dependency-groups"]["dev"]
        license = project["license"]
        authors = [author["name"] for author in project["authors"]]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, license, authors)
