

class MagicModel():
    """
    每个函数没有得到元素的时候返回空list
    
    """
    def __fix_axis():
        # TODO 计算
        self.__model_list = xx
        
    def __init__(model_list:list, page:Page):
        self.__model_list = model_list
        self.__fix_axis()
        self.__page = page
        
    def get_imgs(self, page_no:int): # @许瑞
        
        return_lst = []
        img = {
        "bbox":[x0,y0,x1,y1]
        }
        img_caption = {
        "bbox":[x0,y0,x1,y1],
        "text":"",
        }
        return [{"img":img, "caption":img_caption},]
        
    def get_tables(self, page_no:int) ->list: # 3个坐标， caption, table主体，table-note
        pass # 许瑞
        
    def get_equations(self, page_no:int)->list: # 有坐标，也有字
        return inline_equations, interline_equations  # @凯文
        
    def get_discarded(self, page_no:int)->list: # 自研模型，只有坐标
        pass # @凯文
        
    def get_text_blocks(self, page_no:int)->list: # 自研模型搞的，只有坐标，没有字
        pass # @凯文
        
    def get_title_blocks(self, page_no:int)->list: # 自研模型，只有坐标，没字
        pass # @凯文
        
    def get_ocr_text(self, page_no:int)->list: # paddle 搞的，有字也有坐标
        pass  # @小蒙
        
    def get_ocr_spans(self, page_no:int)->list:
        pass   # @小蒙
       