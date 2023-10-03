# SPDX-FileCopyrightText: 2023-present Francisco Júnior <fjunior.alves.oliveira@gmail.com>
#
# SPDX-License-Identifier: MIT
from checks.check_total_orcamento import check_total_orcamento_fiscal
import logging

LOG_FORMAT = '%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z'
logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT, level=logging.INFO)
