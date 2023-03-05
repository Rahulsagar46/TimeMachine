from timelog.serializers import TeamSerializer
from timelog.serializers import DepartmentSerializer


def create_new_team(team_info):
    serializer = TeamSerializer(data=team_info)
    is_valid = serializer.is_valid()
    if is_valid:
        new_team = serializer.create(serializer.data)
        return (True, new_team)
    else:
        return (False, serializer.errors)


def create_new_department(dept_info):
    serializer = DepartmentSerializer(data=dept_info)
    is_valid = serializer.is_valid()
    if is_valid:
        new_team = serializer.create(serializer.data)
        return (True, new_team)
    else:
        return (False, serializer.errors)
