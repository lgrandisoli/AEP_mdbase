# AEP RFP Knowledge Base

Base de conhecimento em Markdown gerada automaticamente a partir da documentação pública da Adobe Experience Cloud. Utilizada como fonte de contexto para respostas a RFPs (Request for Proposal).

## Produtos cobertos

| Produto | Crawler | Pasta de saída |
|---|---|---|
| Adobe Experience Platform + RT-CDP | `AEPRTCDP_crawler.py` | `aep_guides/` |
| Adobe Journey Optimizer B2C | `ajo_phase_1_crawler_rfp_flat.py` | `ajob2c_guides/` |
| Customer Journey Analytics | `cja_crawler_v4.py` | `cja_guides/` |
| Adobe Target | `target_crawler.py` | `target_guides/` |
| Adobe Workfront | `workfront_crawler_v4.py` | `workfront_guides/` |
| Experience Cloud AI / Agent Orchestrator | `experience_cloud_ai_crawler.py` | `agents_guides/` |

Cada crawler captura a documentação técnica do [Experience League](https://experienceleague.adobe.com) e as Product Descriptions do [helpx.adobe.com](https://helpx.adobe.com/legal/product-descriptions).

## Pré-requisitos

```bash
pip install requests beautifulsoup4
```

## Como executar

### Todos os crawlers de uma vez

```bash
bash run_and_compare.sh
```

O script:
1. Renomeia os consolidados anteriores para `*_old.md`
2. Executa todos os crawlers
3. Gera um arquivo consolidado por produto em `consolidados/`
4. Compara o novo consolidado com o anterior e exibe um resumo das diferenças

### Crawler individual

```bash
python3 cja_crawler_v4.py --output-dir ./cja_guides --max-pages 5000 --delay-s 0.5
```

## Estrutura de saída

```
consolidados/
├── AEP_Consolidado.md
├── AJOB2C_Consolidado.md
├── CJA_Consolidado.md
├── Target_Consolidado.md
├── Workfront_Consolidado.md
├── Agents_Consolidado.md
├── README.md          # índice combinado
└── manifest.json      # metadados de todas as páginas
```

## Fontes

- [Adobe Experience League](https://experienceleague.adobe.com)
- [Adobe Product Descriptions](https://helpx.adobe.com/legal/product-descriptions)
