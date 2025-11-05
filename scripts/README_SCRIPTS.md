# 📜 Guia dos Scripts QGI

Todos os scripts estão organizados por plataforma e função.

---

## 🔬 01_Simulacao_Quantica/

### Scripts Principais

#### `teste.py`
- **Descoberta inicial** da convergência para ln(2)
- **Primeiro script** que revelou o fenômeno espontaneamente
- Simples, sem construções artificiais

#### `testes_prova_de_bala_qgi.py`
- **12 testes "bulletproof"** para validar QGI
- Múltiplas famílias (Haar, Clifford, Brickwork, QFT)
- Múltiplas métricas (Shannon, Rényi-2, Mutual Info)
- Estimadores robustos (MLE, Miller-Madow, NSB)
- Análise de ruído e controles

#### `testes_definitivos_cirurgicos.py`
- **10 testes cirúrgicos** anteriores
- Análise estatística rigorosa
- Bootstrap, AIC/BIC

---

## ☁️ 02_IBM_Quantum/

### Scripts Principais

#### `testes_ibm_quantum_hardware.py`
- **Protocolo completo** para hardware IBM
- Seleção automática de backend
- Mitigação de erros (M3, ZNE)
- **Checkpoint automático** (salva após cada job)
- Suporte para plano Open (sem Sessions)

#### `recuperar_jobs_ibm.py`
- Recupera jobs perdidos
- Reconecta ao IBM e atualiza checkpoint

#### `monitorar_todos_ibm.sh`
- Monitor em tempo real dos testes
- Estatísticas e progresso

---

## 🌀 03_CERN_ATLAS/

### Scripts Principais

#### `qgi_atlas_cirurgico.py`
- **Análise cirúrgica** de dados ATLAS
- Múltiplos proxies de complexidade
- Separação signal/background
- Fits QGI (base, peak, acceleration)
- Bootstrap para ICs

#### `qgi_atlas_controles_finais.py`
- **5 controles estatísticos:**
  1. Teste nulo (shuffle)
  2. Robustez de binning
  3. Sidebands
  4. DATA vs MC
  5. ICs por bootstrap

#### `qgi_atlas_hierarquia_canais.py`
- Análise de múltiplos canais (Z, W, top, Higgs)
- Hierarquia de curvaturas
- Comparação DATA vs MC

---

## 📊 04_Analises/

### Scripts Principais

#### `analisar_resultados_ibm.py`
- Análise estatística dos resultados IBM
- Fits QGI automáticos
- Gráficos de scaling
- Relatórios em Markdown
- Verificação da janela ln(2)

---

## 🚀 Como Usar

### Rodar Testes Simulador
```bash
cd 02_SCRIPTS/01_Simulacao_Quantica/
python3 testes_prova_de_bala_qgi.py --complete
```

### Rodar Testes IBM
```bash
cd 02_SCRIPTS/02_IBM_Quantum/
python3 testes_ibm_quantum_hardware.py --quick
```

### Analisar Dados CERN
```bash
cd 02_SCRIPTS/03_CERN_ATLAS/
python3 qgi_atlas_cirurgico.py
```

### Analisar Resultados IBM
```bash
cd 02_SCRIPTS/04_Analises/
python3 analisar_resultados_ibm.py
```

---

**Todos os scripts estão documentados e prontos para uso!**


