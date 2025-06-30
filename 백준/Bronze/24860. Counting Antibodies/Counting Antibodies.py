V_k, J_k = map(int, input().split())
V_l, J_l = map(int, input().split())
V_h, D_h, J_h = map(int, input().split())

light_combinations = V_k * J_k + V_l * J_l
heavy_combinations = V_h * D_h * J_h

print(light_combinations * heavy_combinations)