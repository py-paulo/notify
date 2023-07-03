# Notify docs

**Notify** é uma biblioteca escrita em *Python* para criar notificações/alertas bem estruturados, oferecendo uma boa interface para o usuário facilitando o *troubleshooting* com detalhes e informações extras, em aplicativos de mensageria, atualmente dando suporte a **Teams** e **Slack**.

## Requisitos

Python 3.6+

## install

Para instalação a partir do código fonte no Gitlab:

<div class="termy">

```console
git clone \
    https://github.com/py-paulo/notify.git
pip install -r requirements.txt
pip install build
python -m build
pip install dist/nofity-<version>.whl
```

</div>


## Guide

Para utilizar a biblioteca basta importar a *class* `Notify` a partir do módulo `notify`:

```python
from notify import Notify
```

O método `init` da classe os serguintes paramêtros:

* `origin_ip: str` O endereço IP da máquina da qual a notificação
está sendo enviado.
* `enable_slack: bool` Habilitar o envio para o **Slack**.
    * `slack_token: str` Requirido.
    * `slack_channel: str` Requirido.
* `enable_telegram: bool` **AINDA NÃO IMPLEMENTADO**.
* `enable_teams: bool` Habilitar o envio para o **Teams**.
    * `teams_webhook_url: str` Requirido.
* `enable_errors: bool` Caso definido como `True` será utilizado a
biblioteca `loguru` como *logging*.

Examplo completo:

```python
from notify import Notify
from notify.constants import ERR_BODY_EXAMPLE, ERR_TITLE_EXAMPLE

if __name__ == '__main__':
    nf = Notify(
        enable_slack=False, enable_teams=True,
        teams_webhook_url='https://webhook.office.com/...')
    nf.log(ERR_BODY_EXAMPLE, title=ERR_TITLE_EXAMPLE)
```

## Testes

### docstest

```console
python -m doctest -v notify/utils.py
```

### lint

```console
pip install lint
pylint notify
```

### flake8

```console
pip install flake8
flake8 . --count --select=E9,F63,F7,F82,E902 \
    --show-source --statistics --max-line-length=120
```

### unnitest

```console
pip install pytest
pytest
```

## Licença

Esse projeto é licenciado sob os termos da licença MIT.
