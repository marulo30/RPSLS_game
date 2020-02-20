# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.shortcuts import render

from random import choice


class HomeView(TemplateView):
	template_name = 'juego_pptls/home.html'

class CreateUserView(CreateView):
	template_name = 'juego_pptls/registro.html'
	form_class = UserCreationForm
	success_url = '/'

	def form_valid(self, form):
		valid = super(CreateUserView, self).form_valid(form)
		username, password = form.cleaned_data['username'], form.cleaned_data['password1']
		new_user = authenticate(username=username, password=password)
		login(self.request, new_user)
		return valid

# Create your views here.
def juegoPptls(request):
	context = {}
	if request.method == 'POST':
		player1 = request.POST['opcion']
		player2 = choice(moves)
		context['resultado'] = calculate_winner(player1, player2)
	return render(request, 'juego_pptls/index.html', context)


MOVES_QUE_PIERDEN ={
	"piedra" : ["lagarto", "tijeras",],
	"papel" : ["piedra", "spock",],
	"tijeras" : ["papel", "lagarto",],
	"lagarto" : ["spock", "papel",],
	"spock" : ["piedra", "tijeras",],
}

moves = MOVES_QUE_PIERDEN.keys()

def calculate_winner(player1, player2):
	if player1 in MOVES_QUE_PIERDEN[player2]:
		return "La maquina eligio %s Player 2 GANA!!\n" % (player2)
	elif player2 in MOVES_QUE_PIERDEN[player1]:
		return "La maquina eligio %s Player 1 GANA!!\n" % (player2)
	else:
		return "EMPATE!!!"