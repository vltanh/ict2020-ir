# Whoosh for News Search

## Info

|Name|Student ID|Mail|
|---|---|---|
|Vũ Lê Thế Anh|20C13002|anh.vu2020@ict.jvn.edu.vn|

## **Setup**

```
conda create -n ir-a2
conda install python=3.9
conda install whoosh
conda install feedparser
pip install underthesea
```

## **Usage**

### **Crawl**

To crawl from RSS source, put the RSS links into a TXT file in multiple lines and use `crawl.py`.

```
usage: crawl.py [-h] -i INPUT

Crawl from RSS links

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to the TXT file containing RSS links
```

It will generate a JSON file containing all the articles.

Example:

```
python crawl.py -i data/rss.txt -o data/articles.json
```

### **Create index**

```
usage: create_index.py [-h] -d DATA [-i INDEX]

Create Whoosh index

optional arguments:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  Path to JSON file containing the articles
  -i INDEX, --index INDEX
                        Directory in which to store the index
```

Example:

```
python create_index.py -d data/articles.json -i indexdir
```

### **Query**

```
usage: query.py [-h] -q QUERY [-i INDEX]

Search Whoosh index

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Query string
  -i INDEX, --index INDEX
                        Directory containing the index
```

Example:

```
python query.py -i indexdir -q bitcoin
```

## **Results**

```
python query.py -i indexdir -q "bitcoin"
```

```
Title: Giá Bitcoin hôm nay 15/3: Bitcoin đảo chiều kéo theo nhiều tiền áo khác cũng tăng mạnh
Link: https://tuoitrexahoi.vn/gia-bitcoin-hom-nay-15-3-bitcoin-dao-chieu-keo-theo-nhieu-tien-ao-khac-cung-tang-manh-197960.html
=====
Title: Giá Bitcoin hôm nay 20/11: Dao động ở mức 58.000 USD
Link: https://tuoitrexahoi.vn/gia-bitcoin-hom-nay-20-11-dao-dong-o-muc-58000-usd-192207.html
=====
Title: Giá Bitcoin hôm nay 14/3: Bitcoin tiếp tục giảm, thị trường rực đỏ
Link: https://tuoitrexahoi.vn/gia-bitcoin-hom-nay-14-3-bitcoin-tiep-tuc-giam-thi-truong-ruc-do-197916.html
=====
Title: Giá Bitcoin hôm nay 13/3: Bitcoin dậm chân tại chỗ, thị trường ảm đạm
Link: https://tuoitrexahoi.vn/gia-bitcoin-hom-nay-13-3-bitcoin-dam-chan-tai-cho-thi-truong-am-dam-197853.html
=====
Title: Giá Bitcoin hôm nay 23/10: Lấy lại 'phong độ' sau những ngày trượt dài, điều chỉnh về mức 60.000 USD
Link: https://tuoitrexahoi.vn/gia-bitcoin-hom-nay-23-10-lay-lai-phong-do-sau-nhung-ngay-truot-dai-dieu-chinh-ve-muc-60000-usd-190509.html
=====
Title: Giá Bitcoin hôm nay 24/10: Rời 'đỉnh lịch sử', trượt dốc xuống dưới 60.000 USD
Link: https://tuoitrexahoi.vn/gia-bitcoin-hom-nay-24-10-roi-dinh-lich-su-truot-doc-xuong-duoi-60000-usd-190555.html
=====
Title: Giá Bitcoin hôm nay ngày 21/10: Đạt kỷ lục hiếm hơn 66.000 USD, thị trường BTC nhộn nhịp
Link: https://tuoitrexahoi.vn/gia-bitcoin-hom-nay-ngay-21-10-dat-ky-luc-hiem-hon-66000-usd-thi-truong-btc-nhon-nhip-190373.html
=====
Title: Giá Bitcoin hôm nay 22/10: Xuống dốc không phanh từ đỉnh cao lịch sử
Link: https://tuoitrexahoi.vn/gia-bitcoin-hom-nay-22-10-xuong-doc-khong-phanh-tu-dinh-cao-lich-su-190425.html
=====
```
