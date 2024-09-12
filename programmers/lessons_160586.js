function solution(keymap, targets) {


        function make_arr(array,where_push)
        {
            for(let i = 0; i < array.length; i++)
            {
                where_push.push([]);
                    for(let j = 0; j < array[i].length; j++)
                        {
                        where_push[i].push(array[i][j]);
                    }
            }
        }

        const map = [];
        const targets_array = [];

            make_arr(keymap,map);
            make_arr(targets,targets_array);

        const result = []

            function find_target(targets_arr)
        {
        let the_smallest= [];
            let return_value = 0;

        for(let i = 0; i < map.length; i++)
        {
                for(let j = 0; j < map[i].length; j++)
                {
                    if(targets_arr == map[i][j])
                    {
                        the_smallest.push(j+1);

                    }
                }
            }


        if(the_smallest.length === 0)
            {
                return [-1];
            }
            else
        {
                return the_smallest;
            }
            }


                for(let i = 0; i < targets_array.length; i++)
        {

        let value = 0;
        for(let j = 0; j < targets_array[i].length; j++)
        {
                value = value + Math.min(...find_target(targets_array[i][j]));
                    if(Math.min(...find_target(targets_array[i][j])) === -1)
                    {
                        value = -1;
                            break;
                    }
            }
            result.push(value);
        }


            console.log(targets_array);
            console.log(result);
            var answer = result;
            return answer;
    }
