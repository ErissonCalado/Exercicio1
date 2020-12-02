# a empresa união_PE vai receber os clientes da empresa união_RN e precisam juntar as agendas dos clientes das 2 empresas. agenda união_PE: {Ruth: 7869-1247, Tatiana: 7496-8541, Caio: 8541-9631}
# agenda união_RN : {Felipe: 6394-7412, Marta:6391-7526}
agenda_pe = {'Ruth': '7869-1247', 'Tatiana': '7496-8541', 'Caio': '8541-9631'}
agenda_rn = {'Felipe': '6394-7412', 'Marta': '6391-7526'}
agenda_uniao = {}

agenda_uniao.update(agenda_pe)
agenda_uniao.update(agenda_rn)
print(agenda_uniao)
