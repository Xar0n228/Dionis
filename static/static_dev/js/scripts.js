//
//
//
//
//
//
//
//
//
//
//
//
//
//
// Загружает элемент только когда  он готов
// $(document).ready(function(){
//     var form = $('#form_buying_product');
//     console.log(form);
//     form.on('submit', function (e) {
//         // e - событыие функции отправки формы
//         e.preventDefault();
//         // чтобы функция больше не отображалась
//         console.log('123');
//         // // выводит в консоль Ф12
//         // prevent_devault
//         // предотвратить проведение фукции
//
//         var nmb = $('number').val();
//         //     //можем вызывать этот элемент
//  // После записи изменений в ХТМЛ, ДЖЕЙКУЭРИ поможет эти записи считать
//         console.log(nmb);
//         var submit_btn = $('#submit_btn');
//         // С неё считываем те дата-атрибуты, которые нам нужны
//         var tovar_id = submit_btn.data("tovar_id");
//
//         var tovar_name = submit_btn.data("name");
//         var tovar_price = submit_btn.data("zena");
//         console.log(tovar_id);
//         console.log(tovar_name);
//
//             var data={};
//             data.tovar_id = tovar_id
//             data.nmb = nmb
//             var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
//             data["csrfmiddlewaretoken"] = csrf_token;
//             var url = form.attr("action");
//             // токен длф пост запросов.
//             $.ajax({
//                  url: url,
//                  type: 'POST',
//                  data: data,
//                  cache: true,
//                  success: function (data) {
//                      // фукнция, которая вызывается если успешно получен ответ с сервера
//                      console.log("OK");
//                      console.log(data.products_total_nmb);
//                      if (data.products_total_nmb || data.products_total_nmb == 0){
//                         $('#basket_total_nmb').text("("+data.products_total_nmb+")");
//                          console.log(data.products);
//                          $('.basket-items ul').html("");
//                          $.each(data.products, function(k, v){
//                             $('.basket-items ul').append('<li>'+ v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + 'грн  ' +
//                                 '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
//                                 '</li>');
//                          });
//                      }
//
//                  },
//             error: function(){
//                  console.log("error")
//              }
//          })
//
//
//
//         $('.basket-items ul').append('<li>'+tovar_name+', '+nmb +'шт.' +'по ' + tovar_price + 'грн  ' +
//             '<a class="delete-item" href="">_/_X_/_</a>' +
//             '</li>');
//         // li - это вставка кода, который мы комбинируем с текстом и переменными
//
//         // добавляем внутрь ещё один элемент
//         // ul - тип элеменрта дальше
//
//         // ..Добавляем переменную
//
//         ///Как в HTML-файле идёт <ul ... <li
//     });
//     // выводит
//  // Описывает событие
//     // САМОПИСНЫЕ ФУНКЦИИ В ДЖЭЙКУЖРИ
//     // мы отслеживаем стандартные элементы джэйкэри и выбираем с помощью селекторов. Применяем их многоприменяемые функции
//
//     function shovingBasket(){
//         ////////////
//          $('.basket-items').toggleClass('hidden');
//     };
//
//     $(".basket-container").on('click',  function (e) {
//         // ОБРАБАТЫВАЕТ СОБЫТИЕ click НА МЫШКЕ
//         e.preventDefault();
//         shovingBasket();
//         // $('.basket-items').removeClass('hidden')
//
//     });
//
//     $(document).on('click', '.delete-item', function (e){
//         e.preventDefault();
//         // this = delete-item
//         $(this).closest('li').remove();
//
//     });
//     //
//     // $(".basket-container").mouseover/(mouseout)(function (e) {
//     //     // событие движения мышкой
//     //     e.preventDefault();
//     //     // $('.basket-items').removeClass('hidden')
//     //
//     // })
// });

//##########################################################################################################################################################

$(document).ready(function() {
    // загружается только тогда, когда HTML-документ будет готов
    var form = $('#_form_buying_product');
    console.log('TEST');//+
        // $- что к данному элементу на странице стоит обращаться как к элементу JQUERRY
    // console.log(form);
        // выводит форму в консоль-лог


    function add_to_order(towar_id, number, is_delete) {

        var data = {};
            // переменная, в которой будут данные, которые мы отправляем
        data.towar_id = towar_id;
            //данные, которые мы получаем при вызове этой функции
        data.number = number;
        var csrf_token = $('#_form_buying_product [name="csrfmiddlewaretoken"]').val();
            //этот код можно считать в переменную. По id-класса формы в шаблоне html
            //мы считывает токен с класса формы
        data["csrfmiddlewaretoken"] = csrf_token;
            //добавляют токен, чтобы делать пост-запрос
        // console.log(csrf_token)
        if (is_delete) {
            data["is_delete"] = true;

        }
        var url = form.attr("action");
        // var url = 'add_to_order';
        console.log(url);//+
            //считываем url с атрибута action на форме
            //в нашем случае считываем url 'orders_name: basket_adding' с шаблона в towar.html

            //адрес, на который необходимо отправлять пост-запрос
        console.log(towar_id);//+
        console.log(data);//+
        $.ajax({
                //для возможности взаимодействия фронтэнда с бэкэнедом без переобновления страницы
                url: url,
                    // ajax, в котором используется url, указанный выше
                type: 'POST',
                    //тип запроса
                data: data,
                    //дата - переменная с данными, которые мы отправляем
                cache: true,
                success: function (data) {
                    //функция, которая вызывается, если успешно получен ответ с сервера
                    console.log("OK");
                    console.log(data.total);
                    //получаем из ORDER/view, где data = dict_for_return, а towars_total_nmb = запись в словаре dict_for_return
                    if (data.total_number) {
                        //   ||=или
                        // условие, если по какой-то причине это значение отсутствует
                        $('#_basket_total_nmb').text("(" + data.total_number + ")");
                            //мы имеем просто html-блок <span>, в который мы вписываем текст
                        console.log(data.towars);

              //С НУЛЯ ОТРИСОВЫВАЕМ ВСЕ ЗАПИСИ В СТРАНИЦЕ. Для этого передаём все записи со страницы на сторону браузера

                        $('.basket-items ul').html("");
                            //весь html код внутри станет пустым. Походу пустыми станут только переменные, т.к работает не как clear
                        // $('.basket-items ul').clear(); - очищает сначала все товары, которые уже имеются в корзине
                            //делает так, что внутри класса basket-items удаляется весь html-код и не будет никаких переменных
                        $.each(data.towars, function (k, v) {
                            //k - ключ/индекс. v - значение/объект
                            //data.towars - это dict(), который мы добавляем из views, где name/number - ключи этого словаря с данными
                            $('.basket-items ul').append('<li>' + v.name + ', ' + v.amount + 'шт. ' + 'по ' + v.single_price + 'грн  ' +
                                //number - count из модели
                                //Добавляем инфу из словаря в класс html-документа.
                                // '<a class="delete-item" href="" data-towar_id="' + v.id + '">x</a>' +
                                // '<a class="delete-item" href="" data-towar_id="{{ towar_in_order.id }}">x</a>' +
                                '<a class="delete-item" href="" data-towar_id="' + v.id + '">x</a>' +
                                '</li>');
                                    //Добавляем в корзину
                                    //Добавляем так, чтобы при нажатии на "х" элемент отправлялся в последующий обработчик delete-item
                        });
                    }

                },
                error: function () {
                    //функция, которая вызывается, если ответ с сервера не получен успешно
                    console.log("error")
                }
        })

    }

    form.on('submit', function (e) {
        //привязывает к форме событие. on-submit, on-сlick, on-change. Набор стандартных событий
        //e - элемент события, элемент отправки формы через submit
        e.preventDefault();
            // предотвращает стандартное поведение
        var number = $('#_number').val();
            // id="number" в форме в towar.html вызываем элемент по его id через #
            //val() - чтобы получить значение этого элемента
        console.log(number);
        var submit_btn = $('#_submit_btn');
            // id="submit_btn" в towar.html
        var towar_id = submit_btn.data("towar_id");
        var name = submit_btn.data("name");
        var price = submit_btn.data("price");
        console.log(towar_id);
        console.log(name);
        console.log(price);

        //$('.basket-items ul').append('<li>'+название_переменной(из var можно)+', ...</li>)
        //добавить в вывод класса
        add_to_order(towar_id, number, is_delete = false)

    });

    function showingBasket() {
        $('.basket-items').removeClass('hidden');
        //.toggleClass - переключает видимость элемента
        //есть целый список методов с сайта JQUERY
    };

    //$('.basket-container').on('click', function(e){
    //    e.preventDefault();
    //    showingBasket();
    //});

    $('.basket-container').mouseover(function () {
        showingBasket();
        //вызывает функцию, так-же, как и def в Python
    });

    $('.basket-container').mouseout(function(){
        $('.basket-items').addClass('hidden');
    });
    //delete-item - название класса, к которому будет срабатывать. Можно указать несколько

    //Поскольку мы ВЫШЕ создавали новый класс delete-item, то мы не можем обратиться к нему напрямую
    //Поэтому мы пишем document и тогда прога заново ищет в документе нужный класс из списка параметров .on('_._')
    $(document).on('click', '.delete-item', function (e) {
        //$(this) - обращение к этому элементу(delete-item)
        //$(this.closest('___')."remove" - ближайший к этому элементу элемент " ___ "
        e.preventDefault();
        towar_id = $(this).data("towar_id");
        // id считываем с дата-атрибута на этой кнопке
        number = 0;
        add_to_order(towar_id, number, is_delete = true)
    });

    function calculatingOrder() {
        var total_basket_amount = 0;

        $('.total-towar-in-order-amount').each(function () {
            total_basket_amount += parseFloat($(this).text());
                //parseFloat - тоже, что и parseInt, но для десятичных, toFixed(_) - число знаков после ,
                    //toFixed(_) делает значение как строку
            // total_basket_amount += parseInt($(this).text());
                //превращает текст в цифры
        });
        $('#_total_basket_amount').text(total_basket_amount.toFixed(2));
    };

    $(document).on('change', 'towars-in-basket-count', function () {
        //вызываем функцию, которая будет считывать текущее кол-во
        var current_number = $(this).val();
            // поскольку мы сейчас в input, то считывает с него нужное значение

        var current_tr = $(this).closest('tr');
            //Находит ближайший ТЭГ(в нашем случае ряд tr) "tr" и присваивает его в переменную cuttent_tr
        // чтобы найти текущую стоимость товара, необходимо сначала найти ячейку с этим товаром
        var current_price = parseFloat(current_tr.find('.towar-price').text()).toFixed(2);
                //parseInt опять же переводит текст в число
            //из этого ряда находит ТЭГ <span> с классом "towar-price" из файла basket.html
        var total_amount = parseFloat(current_number * current_price).toFixed(2);
            // находим общую сумму
        current_tr.find('.total-towar-in-order-amount').text(total_amount);
            //находим текущий ряд и в нём находим ячейку с классом "total-towar-in-order-amount"
            //в этот класс как "text" записываем total_amount
        calculatingOrder();
    });
        // когда всё сделаем, вызываем функцию. Вызываем в самом конце, когда провелись все манипуляции
        // , чтобы ПЕРЕсчиталось общее количество

});

//##########################################################################################################################################################