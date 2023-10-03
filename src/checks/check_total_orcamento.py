import logging
from checks.utils import pp

logger = logging.getLogger(__name__)

def check_total_orcamento_fiscal(base_qdd_fiscal, acoes_planejamento, verbose = None):
    """
    Total do orçamento fiscal e investimento SIGPLAN vs SISOR

    Verificar se o valor total do orçamento (orçamento fiscal e orçamento de 
    investimento das empresas controladas) coincide com a projeção do PPAG 
    para o ano seguinte
    """
    
    sisor = sum([row['VL_LOA_DESP'] for row in base_qdd_fiscal.read_rows()])
    
    sigplan = sum([
                row['vr_meta_orcamentaria_ano0'] 
                for row in acoes_planejamento.read_rows() 
                if row['is_deleted_acao'] == False and row['identificador_tipo_acao_cod'] in [1, 2, 4, 7, 9]
            ])+100

    result = sisor == sigplan
    if not result:
        logger.error(f'O total do sisor ({pp(sisor)}) é diferente do sigplan ({pp(sigplan)}) em {pp(sisor - sigplan)}. Vide detalhes em: https://t.ly/N_7oM')
        return result
    return result
