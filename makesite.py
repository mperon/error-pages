#!/usr/bin/env python

import pathlib
import shutil

import chevron

OUTDIR = pathlib.Path('./dist')
SRCDIR = pathlib.Path('./src')

pages = [
    {
        'id': 400,
        'nm': 'Requisição inválida',
        'desc': 'O servidor não conseguiu processar a requisição'
    },
    {
        'id': 401,
        'nm': 'Não autorizado',
        'desc': 'O recurso solicitado requer autenticação'
    },
    {
        'id': 403,
        'nm': 'Acesso negado',
        'desc': 'O serviço que você está tentando acessar requer autenticação.'
    },
    {
        'id': 404,
        'nm': 'Não encontrada',
        'desc': 'A Página que você tentou acessar não foi encontrada.'
    },
    {
        'id': 500,
        'nm': 'Erro interno',
        'desc': 'Uma condição inesperada foi encontrada. Reporte este erro para ser resolvido.'
    },
    {
        'id': 501,
        'nm': 'Não implementado',
        'desc': 'A função solicitada ainda não foi implementada'
    },
    {
        'id': 502,
        'nm': 'Serviço não disponível',
        'desc': 'O serviço solicitado não está disponível. Reporte este erro para ser resolvido.'
    },
    {
        'id': 503,
        'nm': 'Serviço não disponível',
        'desc': 'O serviço solicitado não está disponível. Reporte este erro para ser resolvido.'
    },
    {
        'id': 520,
        'nm': 'Host Desconhecido',
        'desc': 'O Hostname requisitado é desconhecido. '
    },
    {
        'id': 521,
        'nm': 'Serviço não disponível',
        'desc': 'O serviço solicitado não está disponível. Reporte este erro para ser resolvido.'
    },
    {
        'id': 533,
        'nm': 'Manutenção agendada',
        'desc': 'Este site está em manutenção. Estamos trabalhando para trazê-lo de volta a ativa.'
    },
]

#
if not OUTDIR.is_dir():
    OUTDIR.mkdir(parents=True)

# reads template file
with open(SRCDIR / 'template.tpl', 'r') as f:
    tpl = ''.join(f.readlines())

for pg in pages:
    with open(OUTDIR / '{}.html'.format(pg['id']), 'w') as w:
        rendered = chevron.render(template=tpl, data=pg)
        w.write(rendered)

# copy files
shutil.copy(SRCDIR / 'favicon.ico', OUTDIR / 'favicon.ico')
shutil.copy(SRCDIR / 'style.css', OUTDIR / 'style.css')
shutil.copy(SRCDIR / 'err.png', OUTDIR / 'err.png')

# nginx config
with open(SRCDIR / 'nginx.tpl', 'r') as fn:
    with open(OUTDIR / 'nginx.conf', 'w') as w:
        rendered = chevron.render(fn, {'pages': pages})
        w.write(rendered)
