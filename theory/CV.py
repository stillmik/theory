"""
Q:: Device map
A:: - device_map = how the model is distributed across hardware devices. 
        Instead of model.to("cuda") (which tries to fit EVERYTHING on one GPU) 
        we can use device_map="auto".
    - device_map="auto" Inspects your hardware (how many GPUs, how much VRAM, CPU RAM)
        Splits the model into chunks (layers)
        Places them smartly: GPU(s) → heavy compute parts, CPU → overflow
    - We cam manually define  device_map = { "encoder": 0, "decoder": 1, "lm_head": "cpu" }

"""