"""
Database Models for CRM System
Define data structures for all entities
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Usuario:
    """User model"""
    id: Optional[int] = None
    username: str = ""
    senha_hash: str = ""
    nome_completo: str = ""
    email: str = ""
    nivel_acesso: str = "usuario"  # admin, usuario
    ativo: bool = True
    data_criacao: Optional[datetime] = None

@dataclass
class Cliente:
    """Client model"""
    id: Optional[int] = None
    nome: str = ""
    cpf_cnpj: str = ""
    telefone: str = ""
    email: str = ""
    endereco: str = ""
    observacoes: str = ""
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None

@dataclass
class Venda:
    """Sales/Business model"""
    id: Optional[int] = None
    cliente_id: int = 0
    valor: float = 0.0
    status: str = "em_negociacao"  # em_negociacao, fechado, perdido
    data_venda: Optional[datetime] = None
    forma_pagamento: str = "dinheiro"  # dinheiro, cartao, transferencia
    descricao: str = ""
    data_criacao: Optional[datetime] = None

@dataclass
class Tarefa:
    """Task/Follow-up model"""
    id: Optional[int] = None
    cliente_id: int = 0
    titulo: str = ""
    descricao: str = ""
    data_limite: Optional[datetime] = None
    prioridade: str = "media"  # alta, media, baixa
    status: str = "pendente"  # pendente, concluida
    data_criacao: Optional[datetime] = None

@dataclass
class Anotacao:
    """Quick notes model"""
    id: Optional[int] = None
    usuario_id: int = 0
    conteudo: str = ""
    data_criacao: Optional[datetime] = None

@dataclass
class ConfiguracaoEmpresa:
    """Company configuration model"""
    id: Optional[int] = None
    nome_empresa: str = ""
    logo_path: str = ""
    data_atualizacao: Optional[datetime] = None