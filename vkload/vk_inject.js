(function (){	// обернем все в безымянную функцию, чтобы не создавать глобальных переменных - просто хороший тон
	var observer = new MutationObserver(listModified);	// создаем объект observer -> вызывает listModified при каждом изменении DOM

	var initialList = document.getElementById('initial_list');	// список изначальной музыки на нашей странице
	if (initialList)
	{
		// список уже был заполнен при подключении расширения - добавляем ссылку "Скачать" для каждой записи в нем
		var rows = initialList.children;
		for (var i = 0; i < rows.length; i++)
		{
			addDownloadLink(rows[i]);	// добавляем ссылку
		}

		observer.observe(initialList, {childList: true});	// следим за изменениями в изначальном списке тоже
	}

	// список аудиозаписей при поиске
	var searchList = document.getElementById('search_list');
	if (searchList)
	{
		// search_list изначально всегда пустой, нам нужно только отрабатывать добавление песен в него
		observer.observe(searchList, {childList: true});	// следим за ним
	}

	// вызывается, когда в список песен добавляются (или удаляются) элементы
	function listModified(mutations)
	{
		for (var i = 0; i < mutations.length; i++)
		{
			var mut = mutations[i];
			if (mut.type != 'childList')
			{
				return;
			}
			// пройдемся по добавленным песням
			for (var j = 0; j < mut.addedNodes.length; j++)
			{
				addDownloadLink(mut.addedNodes[j]);
			}
			// удаленные записи - mut.removedNodes игнорируем
		}
	}

	// функция добавляет ссылку "Скачать" к разметке песни
	function addDownloadLink(row)
	{
		var titleNode = row.querySelector('div.title_wrap');	// Исполнитель песни + название
		if (!titleNode)	// если ничего не работает (может, разметка была изменена?)- выйдем
		{
			return;
		}
		var input = row.querySelector('div.play_btn > input');	// найдем input, в котором хранится url
		if (!input)
		{
			return;
		}
		var ref = input.getAttribute('value');	// сам URL файла
		ref = ref.substr(0, ref.indexOf('?'));	// обрежем все после '?', чтобы оставить только ссылку на mp3

		var link = document.createElement('a');
		link.className = 'downloadLink';	// добавим css класс 'downloadLink' для нашей ссылки
		link.textContent = "Скачать";
		link.setAttribute('download', titleNode.textContent + '.mp3');	// имя файла для загрузки
		link.setAttribute('href', ref);
		link.addEventListener('click', function(event){	// при клике на нашу ссылку, отменим запуск проигрывателя
			event.stopPropagation();
		});
		titleNode.appendChild(link);
	}
})();