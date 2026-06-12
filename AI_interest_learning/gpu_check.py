import torch

print("======= CUDA & GPU 硬件检测 =======")
# 1.判断CUDA是否可用
cuda_available = torch.cuda.is_available()
print(f"CUDA 是否可用：{cuda_available}")

if cuda_available:
    # 2.获取GPU数量、名称、显存
    gpu_count = torch.cuda.device_count()
    print(f"GPU 设备总数：{gpu_count}")
    for i in range(gpu_count):
        gpu_name = torch.cuda.get_device_name(i)
        gpu_prop = torch.cuda.get_device_properties(i)
        print(f"\nGPU{i} 名称：{gpu_name}")
        print(f"GPU{i} 总显存：{gpu_prop.total_memory / 1024**3:.2f} GB")
        print(f"GPU{i} CUDA算力：{gpu_prop.major}.{gpu_prop.minor}")
    print(f"\n本机CUDA版本：{torch.version.cuda}")
    print(f"PyTorch编译CUDA版本：{torch.version.cuda}")

    # 3.CPU张量、GPU张量互相迁移对比
    print("\n======= CPU/GPU 张量迁移测试 =======")
    # 在CPU创建张量
    cpu_tensor = torch.randn(2048, 2048)
    print(f"CPU张量设备：{cpu_tensor.device}")

    # 迁移到GPU
    gpu_tensor = cpu_tensor.cuda()  # 等价 .to("cuda")
    print(f"GPU张量设备：{gpu_tensor.device}")

    # GPU张量迁回CPU
    back_cpu = gpu_tensor.cpu()
    print(f"迁回后设备：{back_cpu.device}")
    # 4.现存实时占用查看
    print(f"\n当前GPU已占用现存：{torch.cuda.memory_allocated() / 1024**3:.2f} GB")
    print(f"GPU缓存显存：{torch.cuda.memory_reserved() / 1024**3:.2f} GB")


else:
    print("未检测到可用CUDA GPU，请检查驱动、CUDA、PyTorch版本匹配")