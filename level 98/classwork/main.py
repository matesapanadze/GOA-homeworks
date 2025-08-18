# # 1)შექმენით manual_range ფუნქცია, რომელიც იქნება range ფუნქციის კოლნი, ამ ფუნქციას უნდა ჰქონდეს 3 არგუმენტი, მაგრამ თუ გამოძახებისას გადაეცა მხოლოდ 1 არგუმენტი default-ად start-ის მნიშვნელობა იქნება 0 და step-ის 1. ხოლო 2 არგუმენტის შემთხვევაში მხოლოდ step-ი იქნება 1.

# # გაიხსენეთ, რომ range ფუნქციას გადაეცემა 3 პარამეტრი start, end, step 

# def manual_range(end, start = 0, step = 1):
#     while start <= end - 1:
#         print(start)
#         start += step


#     # for i in range(start, end + 1):
#     #     sum = start + step
#     #     start = sum
#     #     return start    
    

# manual_range(0, 11, -1)


def maskify(cc):
    if len(cc) <= 4:
        return str(cc)
    elif len(cc) > 4:
        print(('#' * (len(cc) - 4)) + cc[-4:-1] + cc[-1])
    elif cc.isnumeric():
        return str(cc)
    
maskify(input())