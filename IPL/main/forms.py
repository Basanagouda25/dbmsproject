from django import forms
from .models import *


class addPlayer(forms.ModelForm):
    class Meta:
        model=players
        fields=['player_id','name','team','bowling_role','batting_role','is_wk']

class addMatch(forms.ModelForm):
    class Meta:
        model=Matches
        fields=['match_id','team1','team2','date','venue']

class addTeam(forms.ModelForm):
    class Meta:
        model=Teams
        fields=['team_id','name','home_ground']

