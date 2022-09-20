from light_malib.utils.logger import Logger
from torch.utils.tensorboard import SummaryWriter

class Monitor:
    '''
    TODO(jh): wandb etc
    TODO(jh): more functionality.
    '''
    def __init__(self,cfg):
        self.cfg=cfg
        self.writer=SummaryWriter(log_dir=cfg.expr_log_dir)
        
    def get_expr_log_dir(self):
        return self.cfg.expr_log_dir
        
    def add_scalar(self,tag,scalar_value,global_step,*args,**kwargs):
        self.writer.add_scalar(tag,scalar_value,global_step,*args,**kwargs)
            
    def close(self):
        self.writer.close()