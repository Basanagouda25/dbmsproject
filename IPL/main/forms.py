from django import forms
from .models import *

class addBowler(forms.ModelForm):
    class Meta:
        model=bowlers
        fields=['player_id','player','team','role']

class addBatsmen(forms.ModelForm):
    class Meta:
        model=batsmen
        fields=['player_id','player','team','role','is_wk']

class addAllrounder(forms.ModelForm):
    class Meta:
        model=allrounder
        fields=['player_id','player','team','bowling_role','batting_role']

class addMatch(forms.ModelForm):
    class Meta:
        model=Matches
        fields=['match_id','team1','team2','date','venue']

class addTeam(forms.ModelForm):
    class Meta:
        model=Teams
        fields=['team_id','name','home_ground']

