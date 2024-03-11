import wandb
from train import main
import os
print("Current working directory:", os.getcwd())
wandb.login(key="38f7789ea6ddf142850d8c141ecbe9ccd74b86e4")

sweep_config = {
    'name':'tyc_3_epochs',
    'method': 'grid'

    }
#57 hyperparams in total
parameters_dict = {
    'num_channels_dae': {'values': [4, 8, 16]}, 'num_timesteps': {'values': [4, 8, 16, 32]},    
    }



parameters_dict.update({
    'image_size': {'value': 256},               'num_channels': {'value': 2},               'num_epoch': {'value': 3},                  'ch_mult': {'value': [1,1,2,2,4,4]},
    'num_res_blocks': {'value': 2},             'batch_size' :{'value': 1},                 'contrast1': {'value': 'T1'},               'contrast2': {'value': 'T2'},
    'ngf': {'value': 32},                       'embedding_type': {'value': 'positional'},  'use_ema': {'value': True},                 'ema_decay':{'value': 0.999},
    'r1_gamma':{'value': 1.},                   'lr_d':{'value': 1e-4},                     'lr_g':{'value': 1.6e-4},                   'lazy_reg':{'value':10},
    'num_process_per_node':{'value':1},         'save_content':{'value':True},              'local_rank':{'value':0},                   'input_path':{'value':'/home/guests/yichen_tang/syndiff/SynDiff_sample_data/snippet'},
    'exp':{'value':'exp_syndiff'},              'save_ckpt_every':{'value':1},             'seed':{'value':1024},                       'resume':{'value':False},
    'centered':{'value':True},                  'use_geometric':{'value':False},            'beta_min':{'value':0.1},                   'beta_max':{'value':20.},
    'n_mlp':{'value':3},                        'attn_resolutions':{'value':(16,)},         'dropout':{'value':0.},                     'resamp_with_conv':{'value':True},
    'conditional':{'value':True},               'fir':{'value':True},                       'fir_kernel':{'value':[1,3,3,1]},           'skip_rescale':{'value':True},
    'resblock_type':{'value':'biggan'},         'progressive':{'value':'None'},             'progressive_input':{'value':'residual'},   'progressive_combine':{'value':'sum'},
    'fourier_scale':{'value':16.},              'not_use_tanh':{'value':False},             'nz':{'value':32},                          't_emb_dim':{'value':32},
    'beta1':{'value':0.5},                      'beta2':{'value':0.9},                      'no_lr_decay':{'value':False},              'save_content_every':{'value':1},          
    'lambda_l1_loss':{'value':0.5},             'num_proc_node':{'value':1},                'node_rank':{'value':0},                    'master_address':{'value':'127.0.0.1'},     
    'port_num':{'value':'6021'},                'output_path':{'value':'/home/guests/yichen_tang/syndiff/sweep'},                       'z_emb_dim': {'value': 32}
    })

sweep_config['parameters'] = parameters_dict

sweep_id = wandb.sweep(sweep_config, project="syndiff_sweep")
wandb.agent(sweep_id, main)

