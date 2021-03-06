from binance.client import Client

try:
    from config_dev import API_BINANCE_KEY, API_BINANCE_SECRET
    
except Exception:
    from config_prod import API_BINANCE_KEY, API_BINANCE_SECRET

client = Client(API_BINANCE_KEY, API_BINANCE_SECRET)

def BUY(symbol,position_size):
    BUSD_balance = client.get_asset_balance("BUSD")
    if float(BUSD_balance['free']) > 20:
        Interger = position_size.split(".")[0]
        decimal = position_size.split(".")[1]
        dec_count = -1
        
        if len(decimal) > 2:
            while True:
                position_size = Interger + "." + decimal[:dec_count]
                if float(position_size) > 0:
                    try:

                        order = client.order_market_buy(
                            symbol=symbol,
                            quantity=position_size
                        )

                        return order

                    except Exception as e:
                        if e.code == -1013:
                            dec_count = dec_count - 1

                        else:
                            print(e.args)
                            return "เกิดข้อผิดพลาด"
                        
        else:
            try:
                order = client.order_market_buy(
                        symbol=symbol,
                        quantity=position_size
                )

                return order
            
            except Exception as e:
                if e.code == -1013:
                    dec_count = dec_count - 1

                else:
                    print(e.args)
                    return "เกิดข้อผิดพลาด"

                
                
def SELL(symbol,position_size=0,sell_all=True):
    POS_SIZE = str(position_size)
    if sell_all:
        sym = symbol.split("BUSD")[0]
        POS_SIZE = client.get_asset_balance(sym)['free']
        Interger = POS_SIZE.split(".")[0]
        decimal = POS_SIZE.split(".")[1]
        dec_count = -1

        while True:
            position_size = Interger + "." + decimal[:dec_count]
            if float(position_size) > 0:
                try:
                    order = client.order_market_sell(
                        symbol=symbol,
                        quantity=position_size
                    )

                    return order
            
                except Exception as e:
                    if e.code == -1013:
                        dec_count = dec_count - 1

                    else :
                        print(e.args)
                        return "เกิดข้อผิดพลาด"
                
            else:
                return "เกิดข้อผิดพลาด"
                
                    

def ReceiveSignals(signal_data_dict):
    if signal_data_dict["SIGNALS"] == "buy":
        try:
            buy_information = BUY(symbol=signal_data_dict["SYMBOL"],position_size=signal_data_dict["POSITION SIZE"])
            if buy_information == "เกิดข้อผิดพลาด":
                return "BUY {} NOT SUCCESS!".format(signal_data_dict["SYMBOL"])
            else:
                return "BUY {} SUCCESS! \nSIZE : {}".format(signal_data_dict["SYMBOL"],signal_data_dict["POSITION SIZE"])
        except Exception as e:
            return "เกิดข้อผิดพลาด {}".format(e.args)

    elif signal_data_dict["SIGNALS"] == "sell":
        try:
            sell_inforamtion = SELL(symbol=signal_data_dict["SYMBOL"])
            if sell_inforamtion == "เกิดข้อผิดพลาด":
                return "SELL {} NOT SUCCESS!".format(signal_data_dict["SYMBOL"])
            else:
                return "SELL {} SUCCESS!".format(signal_data_dict["SYMBOL"])
        except Exception as e:
            return "เกิดข้อผิดพลาด {}".format(e.args)
