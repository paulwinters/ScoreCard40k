import yaml
import glob


def main():
    for file in glob.glob("resources/missionRules/*.yml"):
        print(file)
        with open(file, 'r') as mission_rule_file:
            mission_rule = yaml.safe_load(mission_rule_file)
            print(mission_rule)

    for file in glob.glob("resources/primaryMissions/*.yml"):
        print(file)
        with open(file, 'r') as primary_mission_file:
            primary_mission = yaml.safe_load(primary_mission_file)
            print(primary_mission)



if __name__ == "__main__":
    main()
