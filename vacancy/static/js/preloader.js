/**
 * Главная функция, которая вызывается сразу
 * после загрузки html - файла
 */
(function() {

	const app = {
		initialize : function () {
            app.monitorStatusTask();
		},
        /**
         * Отслеживание статуса выполнения задачи
         */
        monitorStatusTask: function () {

            $.ajax({
                url: "/generate/",
                type: 'GET',
            }).done(function (msg) {
                if ( msg['status'] === "PENDING"){
                    setTimeout(app.monitorStatusTask, 2600 );
                }
                else if ( msg['status'] === "SUCCESS"){
                    window.location = "/vacancy/";
                }
            })
        },


	};

	app.initialize();
}());
