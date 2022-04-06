## MELD ASSIGNMENT PROJECT

_`just for an assigment - don't burn your money on it *_*`_

### problem

- Xây dựng 1 bot thực hiện paper trading với thuật toán momentum hoặc reversal
  trên sàn Binance (đã có api sẵn hỗ trợ paper trading).
- Yêu cầu và hướng dẫn.
    - Sử dụng websocket hoặc REST API.
    - Với bài toán trading trên sàn Binance, chiến lược đơn giản là tại mỗi thời
      điểm trading thì ta xếp hạng các token có mặt trên sàn theo thứ tự
      historical return từ cao xuống thấp và chọn các token có kết quả tốt nhất
      để đầu tư nếu dùng chiến thuật momentum, và ngược lại nếu dùng chiến thuật
      reversal. Chẳng hạn nếu làm momentum theo tần số trading là theo ngày, thì
      tại một thời điểm cố định trong ngày (ví dụ 9h sáng), ta bán toàn bộ các
      token có mặt trong portfolio, sau đó phân phối đều tiền thu được vào một
      số lượng cố định các token mới mua (ví dụ tốp 10 tokens có tốc độ tăng
      trưởng cao nhất trong bảy ngày gần nhất)  và giữ đúng một ngày rồi lại bán
      ra và cứ lặp lại như vậy. Khi xếp hạng các tokens, có thể giới hạn số
      lượng tokens bằng cách loại bỏ các token còn quá mới hoặc có market
      capitalization quá nhỏ.
    - Phân tích sơ lược về chiến thuật
        - TÍnh toán P/L (net profit and loss) và các chỉ số (inventory balance,
          token price etc.) tại từng thời điểm. Trong các tính toán phải đưa phí
          giao dịch vào.
        - Chú ý các tham số chiến lược:  trade frequency, quote price, volume,
          độ trễ là bao nhiêu etc.
        - Không nhất thiết chiến thuật phải tạo ra net P/L dương, vì mục tiêu là
          thiết kế software.
        - Bonus) Làm dashboard để monitor chiến thuật để người quản lý danh mục

### Solution

- Using binance client library to work with binance API through websocket and
  RESTful API depend on action. For example: using socket for order and waiting
  order result, RESTful for some action like check balance
- Dashboard: In the context of an assigment, will
  using [metabase](https://www.metabase.com/) to provide basic chart from
  database #todo
- _`BinanceExchange <----> iTradingBot <----> DataBase ----> Metabase`_

- In case of production need have change in kind of database, sytem scaling
  strategy and BI tool.

### Install

- local
    - git clone git@gitlab.com:phamngocquy97/itradingbot.git
    - configuration [user.conf](user.cfg.template)
    - python3 app.py

- deploy
    - # todo

#### REF: [binance trade bot](https://github.com/edeng23/binance-trade-bot)

### Feedback

Please make an ```issue``` if have any.

### Problem 2

- Xây dựng database và dashboards tương tự như trên cho một hệ sinh thái cụ thể
  là Avalanche. Trong đó mục tiêu là keep track Total value locked (TVL)  chảy
  từ các blockchain khác TỚI Avalanche và TVL chảy TỪ Avalanche ra các
  blockchain khác. Hãy xây dựng kế hoạch để giải quyết bài toán trên. Tham khảo
  dữ liệu thô từ avascan.io trên cho một hệ sinh thái cụ thể là Avalanche. Trong
  đó mục tiêu là keep track Total value locked (TVL)  chảy từ các blockchain
  khác TỚI Avalanche và TVL chảy TỪ Avalanche ra các blockchain khác. Hãy xây
  dựng kế hoạch để giải quyết bài toán trên. Tham khảo dữ liệu thô
  từ [avascan.io](avascan.io)
- Tham khảo:
    - https://dune.xyz/eliasimos/Bridge-Away-(from-Ethereum)
    - https://www.footprint.network/topic/DeFi/Cross-ChainBridge

#### Solution

- Basic Architecture
<img src="https://ucode-bk-dev.s3.ap-southeast-1.amazonaws.com/quypn/block_chain_dashboard.drawio.png" style="height: 360px; width: 640px"/>

- Specifically: Todo

  
