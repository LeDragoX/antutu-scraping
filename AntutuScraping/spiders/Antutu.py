import scrapy


class AntutuSpider(scrapy.Spider):
    name = 'Antutu'
    start_url = 'https://www.antutu.com/en/'
    allowed_domains = [start_url]
    start_urls = [start_url + 'ranking/rank1.htm']

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.31 Safari/537.36 Edg/94.0.992.14'}

    def parse(self, response):
        devices = response.xpath('//*[@id="section1"]/div[2]/div[2]/ul')

        # Device Position
        position = response.xpath(
            '//*[@id="section1"]/div[2]/div[2]/ul[*]/div[2]/li[1]/span[1]/text()').extract()

        # Device Name
        name = response.xpath(
            '//*[@id="section1"]/div[2]/div[2]/ul[*]/div[2]/li[1]/text()').extract()

        # Device Memory
        memory_spec = response.xpath(
            '//*[@id="section1"]/div[2]/div[2]/ul[*]/div[2]/li[1]/span[2]/text()').extract()

        # CPU
        cpu = response.xpath(
            '//*[@id="section1"]/div[2]/div[2]/ul[*]/div[2]/li[2]/text()').extract()

        # GPU
        gpu = response.xpath(
            '//*[@id="section1"]/div[2]/div[2]/ul[*]/div[2]/li[3]/text()').extract()

        # MEM
        mem = response.xpath(
            '//*[@id="section1"]/div[2]/div[2]/ul[*]/div[2]/li[4]/text()').extract()

        # UX
        ux = response.xpath(
            '//*[@id="section1"]/div[2]/div[2]/ul[*]/div[2]/li[5]/text()').extract()

        # Total Score
        score = response.xpath(
            '//*[@id="section1"]/div[2]/div[2]/ul[*]/div[2]/li[6]/text()').extract()

        #print([position, name, memory_spec, cpu, gpu, mem, ux, score])

        for i in range(len(position)):
            yield {
                'position': position[i],
                'name': name[i],
                'memory_spec': memory_spec[i],
                'cpu': cpu[i],
                'gpu': gpu[i],
                'mem': mem[i],
                'ux': ux[i],
                'score': score[i]
            }

        # Useless line
        for device in devices:
            print(device)

        pass
