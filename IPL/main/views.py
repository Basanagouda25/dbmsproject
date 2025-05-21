from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def diplay_team(request,id):
    team=Teams.objects.get(team_id=id)
    bowlers=team.bowlers.all()
    batsmen=team.batsmen.all()
    allrounder=team.allrounder.all()


    return render(request,'team_players.html',{'team':team,'bowlers':bowlers,'batsmen':batsmen,'allrounder':allrounder})
def display_bowler(request,id):
    bowler=bowlers.objects.get(player_id=id)
    return render(request,'display_bowler.html',{'player':bowler})

def display_batsmen(request,id):
    batter=batsmen.objects.get(player_id=id)
    return render(request,'display_batsmen.html',{'player':batter})

def display_Allrounder(request,id):
    rounder=allrounder.objects.get(player_id=id)
    return render(request,'display_allrounder.html',{'player':rounder})

def display_Team(request,id):
    team=Teams.objects.get(team_id=id)
    return render(request,'display_team.html',{'team':team})

def bowlerForm(request):
    if request.method=='POST':
        create_form=addBowler(request.POST)
        if create_form.is_valid():
            bowler=create_form.save(commit=False)
            bowler.save()
            return redirect('display_bowler',id=bowler.player_id)
    else:
        create_form=addBowler()
    return render(request,'bowlerForm.html',{'form':create_form})

def batsmenForm(request):
    if request.method=='POST':
        create_form=addBatsmen(request.POST)
        if create_form.is_valid():
            batter=create_form.save(commit=False)
            batter.save()
            return redirect('display_batsmen',id=batter.player_id)
    else:
        create_form=addBatsmen()
    return render(request,'batsmenForm.html',{'form':create_form})

def allrounderForm(request):
    if request.method=='POST':
        create_form=addAllrounder(request.POST)
        if create_form.is_valid():
            rounder=create_form.save(commit=False)
            rounder.save()
            return redirect('display_Allrounder',id=rounder.player_id)
    else:
        create_form=addAllrounder()
    return render(request,'allrounderForm.html',{'form':create_form})

def teamForm(request):
    if request.method=='POST':
        create_form=addTeam(request.POST)
        if create_form.is_valid():
            team=create_form.save(commit=False)
            team.save()
            return redirect('display_Team',id=team.team_id)
    else:
        create_form=addTeam()
    return render(request,'teamForm.html',{'form':create_form})
