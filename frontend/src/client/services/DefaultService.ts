/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { HiMomResponse } from '../models/HiMomResponse';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Himom
     * @param a
     * @returns HiMomResponse OK
     * @throws ApiError
     */
    public static djangoTutorialUrlsHimom(
        a: number,
    ): CancelablePromise<HiMomResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/himom',
            query: {
                'a': a,
            },
        });
    }

    /**
     * List Weapons
     * @param limit
     * @param offset
     * @returns string OK
     * @throws ApiError
     */
    public static djangoTutorialUrlsListWeapons(
        limit: number = 10,
        offset?: number,
    ): CancelablePromise<Array<string>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/weapons',
            query: {
                'limit': limit,
                'offset': offset,
            },
        });
    }

}
