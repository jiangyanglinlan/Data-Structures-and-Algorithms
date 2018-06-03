import uuid


class HashTable(object):
    def __init__(self):
        # table 是用来存储数据的数组
        # size 最好选素数, 以便于得到更为合理的下标分布
        self.table_size = 10007
        self.table = [0] * self.table_size
        print('table 类型为', type(self.table))
        print('table 长度为', len(self.table))

    # 实现 in not in 语法
    def __contains__(self, item):
        return self.has_key(item)

    def has_key(self, key):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return True
        # 如果得到的是 int 0 说明没有找到, 返回 False
        # 如果得到的是 list 但是遍历结果没有要找的 key 也是 False
        return False

    def _insert_at_index(self, index, key, value):
        # 检查下标处是否是第一次插入数据
        v = self.table[index]
        data = [key, value]
        if isinstance(v, int):
            # 如果是第一次, 得到的是 int 0
            # 那么就插入一个 list 来存, 以后相同的 key 的元素都放这里面
            # 把 key value 作为一个数组保存, 是因为会出现相同 hash 值的 key
            # 这时候就需要比较原始信息来找到相应的数据
            self.table[index] = [data]
        else:
            # 如果不是, 得到的会是 list, 直接 append
            self.table[index].append(data)

    def add(self, key, value):
        # 计算出下标
        index = self._index(key)
        self._insert_at_index(index, key, value)

    def get(self, key, default_value=None):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return kv[1]
        # 如果得到的是 int 0 说明没找到, 返回 default_value
        # 如果得到的是 list 但是遍历结果没有要找的 key 也是没找到
        return default_value

    def _index(self, key):
        return self._hash(key) % self.table_size

    def _hash(self, s):
        n = 1
        f = 1
        for i in s:
            n += ord(i) * f
            f *= 10
        return n


if __name__ == '__main__':
    names = [
        '江洋',
        '林澜',
        '路依依',
        '上海堡垒',
        '铁甲依然在',
        'Flask',
    ]
    ht = HashTable()
    for key in names:
        value = uuid.uuid4()
        ht.add(key, value)
        print(f'add 元素: key = {key}, value = {value}')
    for key in names:
        v = ht.get(key)
        print(f'get 元素: key = {key}, value = {v}')
    print('Flask' in ht)
    print('Django' in ht) 
