from tasks import multiply

s=multiply.delay(4,10)
print(s)
# print(s.get()) ----> cannot execute as no backend is connected in rabbitmq