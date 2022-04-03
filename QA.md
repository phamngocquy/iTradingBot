#### 2.  (Lending) Hãy tìm hiểu cơ chế hoạt động và tính lãi suất của AAVE hoặc Compound Finance. So sánh với Celsius Network và Anchor Protocol để thấy pros and cons của mỗi dApp.

#### 3. (Bridge)  Tim hiểu cách thức hoạt động của một cross-chain bridge (ví dụ RenVM, WBTC) và nêu ra những khó khăn mà việc xây dựng một cross chain bridge như ADAmatic (từ Cardano sang Polygon) có thể gặp phải (technology, security etc.)

1. **Cross-chain bridge**: Cross-chain bridge là cầu nối Cross-chain cho phép
   luân chuyển các tài sản crypto, token hay dữ liệu từ Blockchain này sang
   Blockchain khác.
2. **Cách thức hoạt động của Binance Bridge**:
    1. Binance Bridge nhằm mục đích chuyển đổi những đồng coi được Binance
       Bridge hỗ trợ thành một dạng warapped token để sử dụng trên Binance Chain
       và Binance Smart Chain. Mục tiêu nhăm hỗ trợ người dùng có thể sử dụng
       được các đồng coin khác như BTC, ETH,.. trên hệ sinh thái Binance Chain.
    2. Cách thức hoạt động: Binance Bridge tạo ra các warapped token tỷ lệ 1: 1
       đối với token nguồn trên mạng blockchain gốc. Đồng thời token gốc sẽ bị
       khoá trên mạng blockchian của nó. Cụ thể trong trường hợp muốn chuyển một
       số lượng BTC lên Binance Smart Chain.
        1. _BEP2/BEP20 được vận hành tập trung._
        2. Binance Bridge tạo ra token (BTCB) tương ứng với BTC trên Binance
           Chain/Binance Smart Chain với tỷ lệ 1:1 neo với số lượng BTC đã được
           locked trong Bitcoin blockchain.
           <img src="https://www.kenhbit.com/wp-content/uploads/2022/01/a3bd5cf6-bf70-4604-9ebb-295d39b22b41.png" style="height: 360px; width: 640px"/>
3. **nêu ra những khó khăn mà việc xây dựng một cross chain bridge như
   ADAmatic (từ Cardano sang Polygon) có thể gặp phải (technology, security
   etc.)**
    1. ADAmatic: MELD and VENT are co-leading the development of ADAmatic, a
       pioneer ecosystem project that will connect the prominent Cardano
       blockchain with the Ethereum scaling L2, Polygon chain.
    2. ..can't find anything about the specs documentation

#### 4. (Stablecoin) Liệt kê các phương pháp để bình ổn giá của một stablecoin được backed bởi một fiat currency. Đưa ra đánh giá cá nhân nếu có thể.

1. **Fiat currency**: Tiền pháp định (tiếng Anh: Fiat Money) là tiền tệ được
   chính phủ của một quốc gia phát hành, qui định, công nhận hợp pháp.
2. **Stable coin**: Stablecoin còn được gọi là đồng tiền ổn định. Đây là một
   loại tiền kỹ thuật số được phát triển trên Blockchain và có giá trị ổn định.
   giá của Stablecoin được neo vào một tài sản ổn định khác như vàng hoặc tiền
   pháp định (USD, EUR) hoặc dựa trên một đồng tiền ảo khác ví dụ như trong
   trường hợp của TerraUSD dựa trên LUNA (burned)
    1. Fiat-backed: Mỗi đợn vị đồng stable coin được đảm bảo bởi một tài sản ổn
       định khác như đồng tiền pháp lý (USD, SGD, EUR) hoặc tài sản khác như
       vàng, gọi chung là các tài sản đảm bảo. Những tài sản đảm bào này được
       nắm giữ bở một tổ chức tài chính do bên thứ ba năm giữ.
3. **Các phương pháp bình ổn giá của một stable coin fiat-backed - USDT**:
    1. USDT stabilized price bằng cách, mỗi USDT được bảo trợ bởi một USD tại
       cục dự trữ Tether Limited. Về các thức hoạt động, người dùng sử dụng tiền
       pháp lý để mua 1 USDT, Tether sẽ sinh ra token tương ứng và đồng USDT
       ngường dùng mua được định giá ~ 1 USD.
    2. Đánh giá cá nhân: Đối với trường hợp của USDT, tài sản đảm bảo (USD) sẽ
       được lưu trữ tại Tether Limited. Điều này đi ngược với đặc điểm của công
       nghệ blockchain. Tài sản đảm bảo được lưu trữ tập trung tại một tổ chứ tư
       nhân. Có thể dẫn tới rủi ro về việc thiếu minh bạch trong cách quản lý
       tài sản dự trữ của nhà quản lý.
    