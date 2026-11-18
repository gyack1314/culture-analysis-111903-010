import json,unittest,tempfile,shutil
from pathlib import Path
import pyarrow.parquet as pq
from materials.physical import load_inventory
ROOT=Path(__file__).resolve().parents[1]

class InputMaterials(unittest.TestCase):
    def test_json_parquet_values_and_inventory(self):
        self.assertTrue(load_inventory(ROOT/'inputs'))
        seed=json.loads((ROOT/'inputs/seed.json').read_text(encoding='utf-8'))
        for name,rows in seed.items():
            self.assertEqual(pq.read_table(ROOT/'inputs'/(name+'.parquet')).to_pylist(),rows,name)

    def test_modified_raw_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'inputs';shutil.copytree(ROOT/'inputs',target)
            inv=json.loads((target/'inventory.json').read_text(encoding='utf-8'))
            p=target/inv['files'][0]['path'];p.write_bytes(p.read_bytes()+b'x')
            with self.assertRaisesRegex(ValueError,'摘要'):load_inventory(target)

    def test_domain_material_references_and_edge_states(self):
        seed=json.loads((ROOT/'inputs/seed.json').read_text(encoding='utf-8'))
        actions=json.loads((ROOT/'inputs/actions.json').read_text(encoding='utf-8'))
        marginals=seed['marginals']
        self.assertTrue(any(x['unit']=='devices' for x in marginals))
        self.assertTrue(any(x['count_kind']=='daily_unique' for x in marginals))
        self.assertTrue(any(len(x['set'])==2 for x in marginals))
        self.assertFalse(any(len(x['set'])==3 for x in marginals))
        self.assertTrue(any(x['decision']=='unresolved' for x in seed['audit_pairs']))
        self.assertTrue(all(x['consent_scope']=='show-period' for x in seed['linked_events']))
