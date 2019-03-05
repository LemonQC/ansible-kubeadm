# ansible-kubeadm
利用ansible结合kubeadm部署k8s

## Step 1 集群环境
实验主机为Windows10专业版，I7-8700,32G内存，128G SSD + 1T 机械，利用virtual box 创建两个节点的机器，提示，存储一定要大一点，CPU >=2，否则容易报错
## Step 2 集群信息
k8s版本为v1.13，节点数目为2，pod的网络地址为10.244.0.0/16，最终安装istio镜像，确保主机可以免秘钥登录
利用ssh-keygen和ssh-copyid

| 集群节点          | 名称| 安装的组件|
| ------------ | -------- | ---------------------------------------- |
| 192.168.129.101 | master    | kubeadm, kubectl, kubelet, kube-apiserver, kube-controller-manager, kube-scheduler, etcd, docker, flannel, kube-proxy, coredns |
| 192.168.129.102 | node1   | kubeadm, kubectl, kubelet, docker, flannel, kube-proxy, coredns        |

## Step 3 创建虚拟机
安装vmware，载入ubuntu16.04操作系统，安装ansible，默认后，安装路径在/etc/ansible/下

## Step 4 修改hosts
修改/etc/ansible下的hosts文件，添加分组和主机信息，如hosts所示
## Step 5 创建playbook01.yaml，确定脚本执行顺序
## Step 6 执行check命令，检查完毕后，执行脚本
检查

    ansible-playbook -C playbook01.yaml
    
执行
   
    ansible-playbook playbook01.yaml





