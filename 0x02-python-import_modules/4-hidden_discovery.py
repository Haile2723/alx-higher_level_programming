#!/usr/bin/python3
# 4-hidden_discovery.py
# Haile2723

if __name__ == "__main__":

    import hidden_4
    name = dir(hidden_4)

    for name in names:
        if name[:2] != "__":
            print(name)
