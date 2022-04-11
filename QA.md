#### 1. (DEX) Đối với một DEX sử dụng AMM, từ góc độ design, làm thế nào để giảm price slippage? Và việc tối ưu hoá price slippage có phải lúc nào cũng tốt? Từ góc độ liquidity provider, làm thế nào để giảm thiểu impermanent loss? Hãy so sánh Muesliswap với Uniswap và đưa ra nhận xét.

1. **DEX - Decentralized Exchange**: Là loại sàn giao dịch tiền điện tử được xây
   dựng và hoạt động một cách phi tập trung dựa trên nền tảng blockchain. Một số
   DEX điển hình như Uniswap, PancakeSwap.
2. **AMM- Automated Market Maker**: Là thuật ngữ để chỉ công cụ mang cung cấp
   tính thanh khoản một cách tự động. Trong giao dịch tính thanh khoản nhằm đề
   cập tới việc một tài sản có thể được mua hoặc bán nhanh tróng và liền mạch
   như thế nào. AMM là một thành phần của sàn giao dịch phi tập trung nhằm tự
   động hoá việc cung cấp thanh khoản. Giao thức này thường được xây dựng bằng
   cách sử dụng hợp đồng thông minh, dựa trên một mô hình toán học (thuật toán)
   để xác định giá của các crypto currency và cung cấp tính thánh khoán.
3. **Impermanent loss**:  là sự suy giảm giá trị tiền điện tử ký quỹ ban đầu khi
   cung cấp thanh khoản cho các AMM (Auto Market Maker). Điều này xảy ra do tỷ
   lệ giữa cặp tài sản được cung cấp thanh khoản thay đổi khi thị trường biến
   động mạnh. Impermanent loss là một trong những khuyết điểm đặc trưng của các
   AMM so với sàn giao dịch truyền thống. Do bản chất của các AMM vốn không có
   các sổ lệnh mà chỉ là một pool chứa các cặp tiền điện tử, khi có một giao
   dịch rút một lượng tiền điện tử ra khỏi pool, điều này làm tỷ lệ coin trong
   cặp tiền điện tử có trong pool bị thay đổi. Điều này có thể dẫn đến tổn thất
   của những người cung cấp thanh khoản.
4. **Price-Slippage**: Là chênh lệch giá giữa thời điểm gửi giao dịch và khi
   giao dịch được xác nhận trên blockchain. Có hai trường hợp phổ biến tạo ra
   trượt giá khi giao dịch trên DEX.\
    1. Khối lượng giao dịch lớn: Thường có độ trễ giữa thời gian người dùng xác
       nhận giao dịch và blockchain xác nhận giao dịch. Giá có thể có thay đổi
       trong khoảng thời gian này.
    2. Tính thanh khoản thấp: Một số giao dịch lớn, sẽ làm mất cân bằng tính
       thanh khoảng giữa các nhóm tài sản. Điều này sẽ ảnh hướng tới giá trong
       quá trình thực hiện giao dịch.
5. **Giảm Price Slippage từ góc độ thiết kế hệ thống**: Giảm thiểu độ trễ của
   việc xác thực giao dich trên blockchain. Ethereum layer 2 là một giải pháp
   tốt về cả tốc độ, tính bảo mật và chi phí.
6. **Việc tối ưu hoá price slippage có phải lúc nào cũng tốt**: Xét từ góc độ
   tối ưu hoá price slippage bằng việc tăng tốc xác nhận giao dịch trên
   blockchain. Nhìn chung, không phải việc tốt ưu hoá price slippage không phải
   lúc nào cũng tốt.Có một số đánh đổi cần chú ý. Việc tăng tốc xác nhận giao
   dịch đồng nghĩa với việc tăng gas giao dịch hoặc giảm node xác nhận giao dịch
    - dẫn tới rủi ro về bảo mật. Luôn có đánh đổi. Một giải pháp tối ưu cho
      trường hợp này là thời gian và chi phí xác nhận giao dịch sẽ tỷ lệ thuận
      với khối lượng giao dịch.
7. **Giảm impermanent loss từ góc bộ liquidity provide**:
    - Chọn những pool thanh khoản có lợi nhuận lớn hơn Impermanent Loss.
    - Ngừng cung cấp thanh khoản khi thị trường sắp biến động mạnh
8. **So sánh Muesliswap với Uniswap và đưa ra nhận xét**:
    1. UNISWAP:
        1. Based on Ethereum
        2. Hoạt động dựa trên một thiết kế có tên gọi là Constant Product Market
           Maker (Công cụ Tạo lập Thị trường Sản phẩm Không đổi), một biến thể
           của mô hình Công cụ Tạo lập Thị trường Tự động (Automated Market
           Marker - AMM).
        3. Listed more than 1600 crypto token
    2. Muesliswap:
        1. Based on Cardano
        2. Muesli Swap hoạt động mô hình EUTxO trên chuỗi Cardano cho phép sử
           dụng quyền mua giới hạn (Limit).

#### 2.  (Lending) Hãy tìm hiểu cơ chế hoạt động và tính lãi suất của AAVE hoặc Compound Finance. So sánh với Celsius Network và Anchor Protocol để thấy pros and cons của mỗi dApp.

1. **AAVE**: AAVE là một hệ thống cho vay phi tập chung (decentralized lending
   system_) cho phép người có thể vay, cho vay và kiếm lãi từ tài sản điện tử,
   tất cả các hoạt động của người dùng đều không có người trung gian.
2. **AAVE Cơ chế hoạt động và tính lãi suất**:
    1. Lending Pool: Lending pool chính là khoản cho hay ngang hàng P2P, được
       thiết lập bằng các hợp đồng thông minh trên Blockchain. Điều này cho phép
       người dùng (untrusted users) có thể vay và cho vay tài sản điện
       tử.<img src="https://ucode-bk-dev.s3.ap-southeast-1.amazonaws.com/quypn/Screen+Shot+2022-04-05+at+23.21.31.png" style="height: 320px; width: 640px">
    2. AAVE protocol: Với core là lending pool, AAVE còn bổ sung giao thức mới
       chuyển đổi từ người dùng cá nhân sang nhóm cho vay hoặc đi vay.
        1. Nhóm đi vay và nhóm cho vay tương tác bởi AAVE Protocol với ba thành
           tố tạo nên gồm Price Oracle (Mức giá dự phòng), Collateral
           Liquidators (Người thanh lý tài sản thế chấp) , Integrated
           Applications (Ứng dụng tích hợp).
            - Lãi suất cho cả người đi vay và người cho vay được quyết định theo
              thuật toán
            - Đối với người đi vay, nó phụ thuộc vào chi phí tiền tệ – số tiền
              có sẵn trong nhóm tại một thời điểm cụ thể. Khi tiền được vay từ
              nhóm, số tiền có sẵn sẽ giảm đi, điều này làm tăng lãi suất.
            - Đối với người cho vay, lãi suất này tương ứng với tỷ lệ kiếm được,
              với thuật toán bảo vệ dự trữ thanh khoản để đảm bảo rút tiền bất
              kỳ lúc nào.
            - Quá trình quản trị của token AAVE được mô tả trong hình
              sau: <img src="https://coin68.com/wp-content/uploads/2021/01/qua-trinh-quan-tri-cua-aave-la-gi.png" style="height: 320px; width: 480px" >
        2. Đặc điểm nổi bật của AAVE: Dự án cho phép mọi người vay và cho vay
           bằng khoảng 20 loại tiền điện tử. Một trong những sản phẩm hàng đầu
           của Aave là Flash Loans và Rate Switching.
            + Flash Loans: Aave cho phép các khoản vay không cần thế chấp bằng
              cách tạo ra các logic với điều kiện nếu khoản vay không được hoàn
              trả trong block time thì giao dịch sẽ bị đảo ngược.
            + Rate switching: cho phép người vay (borrowers) chuyển đổi tỷ lệ
              lãi suất cố định hoặc biến động. Thông thường, lãi suất DeFi khá
              biến động làm cho việc ước lượng các chi phí vay dài hạn cũng trở
              nên khó khăn.
                - Nếu người dùng dự đoán lãi suất sẽ tăng, họ có thể chuyển đổi
                  khoản vay sang hình thức fixed rate (tỷ lệ cố định) để khoá
                  chi phí vay trong tương lai.
                - Nếu người dùng nghĩ tỷ lệ lãi suất giảm, họ có thể chuyển đổi
                  lại tỷ lệ biến động để giảm chi phí vay.
3. **So sánh với Celsius Network và Anchor Protocol để thấy pros and cons của
   mỗi dApp.**
    1. Celsius Network
        - Pros:
            - Hệ sinh thái tốt và thân thiện
            - Nhiều dịch vụ không tính phí
            - Cộng đồng sử dụng lớn (22.8B $, 1.7M users)
        - Cons:
            - Có tính kiểm soát tập trung
            - Không có native exchange
            - Hỗ trợ một số lượng hạn chế các loại crypto currency
            - Chưa niêm yết trên các sàn lớn như Binance, Coinbase

    2. Anchor Protocol
        - Pros:
            - Lãi suất gửi tiết kiệm trên Anchor Protocol cao, lên tới 20%/năm
              và có thể rút tiền linh hoạt bất kỳ lúc nào.
            - Người nắm giữ ANC còn có quyền được tham gia vào quản trị nền
              tảng, được hưởng % từ phí giao dịch thu được của nền tảng, dân chủ
              hóa cao hơn so với những token khác.
            - Bỏ qua trung gian, chống kiểm duyệt, có thể giao dịch mọi lúc ở
              mọi nơi với dữ liệu luôn minh bạch và chính xác.
            - Bảo mật là ưu tiên cao nhất của Anchor Protocol
        - Cons:
            - Chưa niêm yết trên coinbase, khó tiếp cận các nhà đầu tư từ US.
            - Dự án còn khá mới, cần thời gian để chứng minh tính bền vững
    3. AAVE
        - Pros:
            - Có nhiều tổ chức uy tính bảo chứng: Blockchain Capital, DTC
              Capital, Three Arrows Capital...
            - AAVE được xây dựng dựa trên tiêu chuẩn ERC-20, và chúng được thiết
              kế để giảm phát.
            - AAVE chạy trên mạng Ethereum, một nền tảng phổ biến bậc nhất.
        - Cons:
            - Một số quy tắc như đặt cọc, lãi suất cũng là trở ngại đối với
              Aave.
            - Aave phải đối mặt với nhiều đối thủ cạnh tranh trong thị trường
              Defi.
            - Giá AAVE coin có xu hướng biến động mạnh và chịu ảnh hưởng từ thị
              trường.

   Nhìn chung so với ANC và CLE. AAVE là dự án tương đối mới và tiềm năng, có ưu
   thế về mặt công nghệ khi có công
   nghệ [layer-2](https://coin98.net/layer-2-la-gi) và chạy trên mạng Ethereum
   là một Blockchain phổ biến bậc nhất hiện nay, đem lại lợi thế về mặt hệ sinh
   thái cho AAVE khi có thể liên kết với nhiều ứng dụng khác trên cùng mạng này.

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
    3. **Nêu ra những khó khăn mà việc xây dựng một cross chain bridge như
       ADAmatic (từ Cardano sang Polygon) có thể gặp phải (technology, security
       etc.)**
       _ADAmatic: MELD and VENT are co-leading the development of ADAmatic, a
       pioneer ecosystem project that will connect the prominent Cardano
       blockchain with the Ethereum scaling L2, Polygon chain._
        1. Security problem: Cross-chain là mục tiêu tấn công của hacker trong
           thời gian gần đây. Một số vụ tấn công điển hình như Wormhole Bridge
           Exploit, Qubit Bridge Exploit, Meter.io Bridge Exploit, Ronin Bridge
           Exploit etc. Sơ đồ tấn công phổ biến vào cross-chain
           bridge <img src="https://ucode-bk-dev.s3.ap-southeast-1.amazonaws.com/quypn/Screen+Shot+2022-04-07+at+02.39.22.png" alt="Common attack vector on Bridges">
           Mặc dù ADAmatic triển khai trên công nghệ layer-2 của Ethereum với
           nhiều ưu điểm về bảo mật và tốc độ, nhưng không thể phủ nhận nguy cơ
           bị tấn công.

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
3. **Các phương pháp bình ổn giá của một stable coin fiat-backed**: Ngoài việc
   neo vào một loại tài sản hay tiền pháp định như cách làm của Tether. Một số
   stablecoin khác bình ổn giá dựa vào các cơ chế Algorithmic. Một số stablecoin
   điển hình như Terra, DAI, AMPL...Algorithmic ở đây hiểu đơn giản là các thuật
   toán có chức năng tự động bình ổn giá. Dựa vào việc điều chỉnh nguồn cung,
   burn token...Ví dụ: Đối với TerraUSD, là một algorithmic stablecoin và chi
   phí để tạo ra một stablecoin bằng đúng với mệnh giả của stablecoin được đúc.
   Để đúng một TerraUSD cần phải đốt số lượng LUNA trị giá 1 USD tại thời điểm
   đó.

[//]: # (    1. USDT stabilized price bằng cách, mỗi USDT được bảo trợ bởi một USD tại)

[//]: # (       cục dự trữ Tether Limited. Về các thức hoạt động, người dùng sử dụng tiền)

[//]: # (       pháp lý để mua 1 USDT, Tether sẽ sinh ra token tương ứng và đồng USDT)

[//]: # (       ngường dùng mua được định giá ~ 1 USD.)

[//]: # (    2. Đánh giá cá nhân: Đối với trường hợp của USDT, tài sản đảm bảo &#40;USD&#41; sẽ)

[//]: # (       được lưu trữ tại Tether Limited. Điều này đi ngược với đặc điểm của công)

[//]: # (       nghệ blockchain. Tài sản đảm bảo được lưu trữ tập trung tại một tổ chứ tư)

[//]: # (       nhân. Có thể dẫn tới rủi ro về việc thiếu minh bạch trong cách quản lý)

[//]: # (       tài sản dự trữ của nhà quản lý.)

	
