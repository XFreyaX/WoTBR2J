# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Embedded file name: scripts/common/battle_results/frontline.py
from battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from DictPackers import ValueReplayPacker
BATTLE_RESULTS = [
 (
  'creditsAfterShellCosts', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'unchargedShellCosts', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'prevMetaLevel', tuple, (0, 1, 0), None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'metaLevel', tuple, (0, 1, 0), None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'flXP', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'originalFlXP', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'subtotalFlXP', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'boosterFlXP', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'boosterFlXPFactor100', int, 0, None, 'any', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'flXPReplay', str, '', ValueReplayPacker(), 'skip', ENTRY_TYPE.ACCOUNT_ALL)]