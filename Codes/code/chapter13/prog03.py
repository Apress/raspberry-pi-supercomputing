from scipy import misc

misc.imshow(misc.imfilter(misc.face(), 'edge_enhance_more'))
