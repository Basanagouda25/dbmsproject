from django.db import models

teams=[
    ('rcb','RCB'),
    ('csk','CSK'),
    ('rr','RR'),
       ]

class Teams(models.Model):
    team_id=models.CharField(primary_key=True)
    name=models.CharField(unique=True)
    home_ground=models.CharField()

    def __str__(self):
        return self.name



class bowlers(models.Model):
    types=[
        ('LHS','left handed spinner'),
        ('RHS','right handed spinner'),
        ('LHP','left handed pacer'),
        ('RHP', 'right handed pacer'),
    ]
    player_id=models.CharField(primary_key=True)
    player=models.CharField()
    team=models.ForeignKey(Teams,  on_delete=models.CASCADE, related_name='bowlers')
    role=models.CharField(choices=types, default='unknown')


    
class batsmen(models.Model):
    types=[
        ('RH','Right hand'),
        ('LH','Left hand'),
    ]
    player_id=models.CharField(primary_key=True)
    player=models.CharField()
    team=models.ForeignKey(Teams,  on_delete=models.CASCADE, related_name='batsmen')

    is_wk=models.BooleanField(default=False)
    role=models.CharField(choices=types, default='unknown')

    
class allrounder(models.Model):
    
    bowling_type=[
        ('LHS','left handed spinner'),
        ('RHS','right handed spinner'),
        ('LHP','left handed pacer'),
        ('RHP', 'right handed pacer'),
    ]
    batting_type=[
        ('RH','Right hand'),
        ('LH','Left hand'),
    ]
    player_id=models.CharField(primary_key=True)
    player=models.CharField()
    team=models.ForeignKey(Teams,  on_delete=models.CASCADE, related_name='allrounder')
    bowling_role=models.CharField(choices=bowling_type, default='unknown')
    batting_role=models.CharField(choices=batting_type,default='unknown')


class Matches(models.Model):
    match_id=models.CharField(primary_key=True)
    team1=models.CharField()
    team2=models.CharField()
    date=models.DateField()
    venue=models.CharField()


