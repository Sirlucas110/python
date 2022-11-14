hr_Inicial= int(input("Digite a hr inicial do jogo: "))
min_Inicial= int(input("Dgite o minuto inicial: "))
hr_Termino= int(input("Digite a hr do término do jogo: "))
min_Termino= int(input("Digite o minuto do termino"))
hrMinutos= hr_Inicial * 60
horaTotal= hrMinutos + min_Inicial
hrMinutos_termino= hr_Termino * 60 + min_Termino
tempPartida= hrMinutos_termino - horaTotal
tempPartidaHR= tempPartida / 60
totalMinDia= 24 * 60
if tempPartidaHR < totalMinDia:
  print("A duraçao do jogo foi de ", tempPartidaHR)
elif tempPartidaHR >= totalMinDia:
  print("A partida acabou no outro dia")